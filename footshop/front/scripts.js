document.addEventListener("DOMContentLoaded", ()=>{

    const track = document.querySelector('.carousel-track');
    const slide = document.querySelectorAll('.carousel-track img');
    const prevbtn = document.querySelector('.carousel-button.prev');
    const nextbtn = document.querySelector('.carousel-button.next');
    let currentIndex = 0;

    function updateCarousel(){
        const slideWidth = slide[0].offsetWidth;
        track.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
        
    }

    prevbtn.onclick = ()=>{
        currentIndex = (currentIndex - 1 + slide.length) %slide.length;
        updateCarousel();
    };

    nextbtn.onclick = ()=>{
        currentIndex = (currentIndex + 1) %slide.length;
        updateCarousel();
    };

    window.onresize = updateCarousel;
    updateCarousel();

    const sneakerslink = document.getElementById('sneakers-link');
    const submenucontainer = document.getElementById('submenu-container')
    const submenu = document.getElementById('submenu')

    sneakerslink.addEventListener('click',(e)=>{
        e.preventDefault();
        submenucontainer.style.display = 'flex';
    });

    submenucontainer.addEventListener('click',(e)=>{
        if(!submenu.contains(e.target)){
            submenucontainer.style.display = 'none';
        }
    });

    
});