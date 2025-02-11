function Randomizer(min, max){
    return Math.floor(Math.random() * (max - min + 1) + min);
}

function mainImageChooser(){
    const main = document.getElementsByTagName('main')[0];
    if (main.id == "galery-main") return;
    let random_number = Randomizer(1, 13)
    console.log(random_number);
    main.style.background = "url({% static 'src/image" + random_number + ".jpg' %}) no-repeat center";
    main.style.backgroundSize = "cover";
    console.log(main.style.background);
}

mainImageChooser();