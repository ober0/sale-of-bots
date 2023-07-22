let buy_btn = document.getElementById("buy");
let tg = window.Telegram.WebApp;
tg.expand()
buy_btn.addEventListener("click", () => {
    let name = document.getElementById('user_name').value;
    let telegram_id = document.getElementById('telegram_id').value;
    let email = document.getElementById('email').value;
    let text = document.getElementById('text').value;
    let time = 0
    if (document.getElementById("three-day").checked){
        time = 3
    }
    if (document.getElementById("seven-day").checked){
        time = 7
    }
    if (document.getElementById("three-week").checked){
        time = 21
    }
    if (document.getElementById("none-day").checked){
        time = 100
    }
    let data1 = {
        name:name,
        telegram_id:telegram_id,
        email:email,
        text:text,
        time:time
    }
    if(name.length < 3){
        alert('Ошибка в имени')
    }
    else if(telegram_id.length < 1){
        alert('Ошибка в вашем телеграмми')
    }
    else if(email < 5){
        alert('Ошибка в Email')
    }
    else{
        if(time != 0){
            alert('Спасибо. С вами свяжутся')
            tg.sendData(JSON.stringify(data));
            setInterval( () => tg.close(),3000);
        }else{
            alert('Не выбран срок готовности')
        }

    }

});

