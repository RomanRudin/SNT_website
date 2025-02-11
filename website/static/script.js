function Randomizer(min, max){
    return Math.floor(Math.random() * (max - min + 1) + min);
}

function mainImageChooser(){
    const main = document.getElementsByTagName('main')[0];
    if (main.id == "galery-main") return;
    main.style.background = "url({% static 'src/image" + Randomizer(1, 13) + ".jpg' %}) no-repeat center";
    main.style.backgroundSize = "cover";
}

mainImageChooser();