// Sale 
document.addEventListener('DOMContentLoaded', () => {
    const sale = new Date('Dec 1 2023 00:00:00');

    const Days = document.getElementById("days");
    const Hours = document.getElementById("hours");
    const Minutes = document.getElementById("minutes");

    const timeCount = () => {
        let currentDate = new Date();
        let leftuntil = sale - currentDate;

        let days = Math.floor(leftuntil / 1000 / 60 / 60 / 24);
        let hours = Math.floor(leftuntil / 1000 / 60 / 60) % 24;
        let minutes = Math.floor(leftuntil / 1000 / 60) % 60;

        Days.textContent = days;
        Hours.textContent = hours;
        Minutes.textContent = minutes;
    };

    timeCount();
    setInterval(timeCount, 1000);
});

// Map

function init() {
    let map = new ymaps.Map('map-test', {
        center: [49.81851950582314,73.10438656309748],
        zoom: 17,
    });
}

function scrollToSection3() {
    var section  = document.getElementById('section3');
    section.scrollIntoView({ behavior: 'smooth'});
}


ymaps.ready(init);