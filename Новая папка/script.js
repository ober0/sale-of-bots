let buy_btn = document.getElementById("buy");
let tg = window.Telegram.WebApp;
tg.expand()
buy_btn.addEventListener("click", () => {
    let name = document.getElementById('user_name').value;
    let telegram_id = document.getElementById('telegram_id').value;
    let email = document.getElementById('email').value;
    let text = document.getElementById('text').value;

    let data1 = {
        name:name,
        telegram_id:telegram_id,
        email:email,
        text:text,
    }
    if(name.length < 3){
        alert('ds')
    }
    else if(telegram_id.length < 1){
        alert('ds')
    }
    else if(telegram_id.length < 1){
        alert('ds')
    }
    else if(telegram_id.length < 1){
        alert('ds')
    }

    else{
        alert('Спасибо. С вами свяжутся')
        tg.sendData(JSON.stringify(data));
        setInterval( () => tg.close(),3000);
    }

});

