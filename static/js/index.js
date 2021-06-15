$(function initListeners() {
  const $userTextForm = $("#textInputForm");
  const $userTextInput = $("#textInput");
  const $transriptionResults = $("#transcriptionResult");
  const $clearResults = $("#clearResults");
  const $nextStepBtn = $("#nextStepBtn");
  const $submitBtn = $("#submitBtn");
  const $prevStepBtn = $("#prevStepBtn");
  const $textInpuitLabel = $("#textInputLabel");
  const $letterChooserLabel = $("#letterChooserLabel");
  const $letterChooser = $("#letterChooser");
  const $modePicker = $("#transcriptionMode");
  const $clearUserText = $("#clearUserText");

  const vowels = ["а", "о", "е", "и", "у", "і", "я", "ю", "є", "ї"];

  let pickedLetters = [];

  $prevStepBtn.on("click", function showPrevStep(event) {
    event.preventDefault();

    $nextStepBtn.show();
    $textInpuitLabel.show();
    $prevStepBtn.addClass("d-none");
    $submitBtn.addClass("d-none");
    $letterChooserLabel.addClass("d-none");

    $userTextInput.show();
    $clearUserText.show();
    $letterChooser.addClass("d-none");

    pickedLetters = [];
    $letterChooser.html("");
  });

  $nextStepBtn.on("click", function showNextStep(event) {
    event.preventDefault();

    const userText = $userTextInput.val().trim();
    if (userText.length !== 0) {
      $nextStepBtn.hide();
      $textInpuitLabel.hide();
      $clearUserText.hide();
      $submitBtn.removeClass("d-none");
      $letterChooserLabel.removeClass("d-none");
      $prevStepBtn.removeClass("d-none");

      $userTextInput.hide();
      $letterChooser.removeClass("d-none");

      userText.split("").forEach(function makeLetterElement(letter, index) {
        if (/(\r\n|\n|\r)/.test(letter)) {
          $letterChooser.append("<br/>");
        } else if (letter.trim().length === 0) {
          $letterChooser.append("&nbsp;");
        } else if (vowels.includes(letter.toLowerCase())) {
          $letterChooser.append(
            `<span data-letterid="${index}" class="letter-chooser__letter">${letter}</span>`
          );
        } else {
          $letterChooser.append(letter);
        }
      });

      $(".letter-chooser__letter").on("click", function saveLetterId() {
        const $thisLetter = $(this);
        const letterId = $thisLetter.data("letterid");

        if ($thisLetter.hasClass("picked-letter")) {
          $thisLetter.removeClass("picked-letter");
          pickedLetters = pickedLetters.filter((item) => item !== letterId);
        } else {
          $thisLetter.addClass("picked-letter");
          pickedLetters.push(letterId);
        }
      });
    } else {
      alert("Введіть текст.");
    }
  });

  $submitBtn.on("click", function sendUserText(event) {
    event.preventDefault();

    $prevStepBtn.prop("disabled", true);
    $submitBtn.prop("disabled", true);
    $clearResults.prop("disabled", true);
    $modePicker.prop("disabled", true);

    const url = $userTextForm.attr("action");
    const userText = $userTextInput.val().trim();
    const mode = $modePicker.val();

    $.post(url, {
      userText,
      pickedLetters: pickedLetters.join(","),
      transcriptionMode: mode,
    })
      .done(function handleRequest(data) {
        $transriptionResults.val(data.transcriptedText);

        $prevStepBtn.prop("disabled", false);
        $submitBtn.prop("disabled", false);
        $clearResults.prop("disabled", false);
        $modePicker.prop("disabled", false);
      })
      .fail(function handleError() {
        alert("Під час роботи програми сталася помилка. Спробуйте ще раз.");

        $prevStepBtn.prop("disabled", false);
        $submitBtn.prop("disabled", false);
        $clearResults.prop("disabled", false);
        $modePicker.prop("disabled", false);
      });
  });

  $clearResults.on("click", function clearResults() {
    $transriptionResults.val("");
  });

  $clearUserText.on("click", function clearText(event) {
    event.preventDefault();
    $userTextInput.val("");
  });
});
