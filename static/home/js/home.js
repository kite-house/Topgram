function dark_light(){
  document.body.classList.toggle("dark-mode");
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

var userTimezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
var csrftoken = getCookie('csrftoken');

fetch('/save_timezone/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': csrftoken,
  },
  body: JSON.stringify({ timezone: userTimezone }),
});

$.ajaxSetup({
  headers: {
    "X-CSRFToken": getCookie("csrftoken")
  }
});

$(document).ready(function () {
  $("#input_message").on("submit", function (event) {
    var $form = $(this);
    event.preventDefault();
    document.getElementById('emoji-menu').style.display = 'none';
    $.ajax({
      url: document.URL,
      type: "post",
      data: $form.serialize(),
      success: function(data){
        $("body").html(data);
      }
    });
  });
});

$(document).ready(function () {
  const emojiIcon = document.getElementById('emoji-icon');
  const emojiMenu = document.getElementById('emoji-menu');

  emojiIcon.addEventListener('click', function() {
    if (emojiMenu.style.display === 'block'){
      emojiMenu.style.display = 'none';
    } else {
      emojiMenu.style.display = 'block';
    }
  });
});

function insertEmoji(emoji) {
  var input = document.getElementById('input_message_field');
  input.value += emoji;
}

function deleteMessage(message_id) {
  $.ajax({
    url: document.URL,
    type: "post",
    data: {
      delete_message: message_id
    },
    success: function(data){
      $("body").html(data);
    }
  });
}

function deleteChat(chat_id) {
  $.ajax({
    url: document.URL,
    type: "post",
    data: {
      delete_chat: chat_id
    },
    success: function(data){
      $("body").html(data);
    }
  });
}