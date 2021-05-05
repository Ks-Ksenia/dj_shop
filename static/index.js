let menu = document.querySelectorAll('.menu');

for (let m of menu){
    m.onmouseover = function(event){
        let target = event.target;
        let parentTarget = target.closest('.topmenu');
        let tag_a = parentTarget.firstElementChild
        console.log(tag_a)
        tag_a.style.background = '#6d068f';
        tag_a.style.width = '91%';
        tag_a.style.color = '#fff';
    };

    m.onmouseout = function(event){
        let target = event.target;
        let parentTarget = target.closest('.topmenu');
        let tag_a = parentTarget.firstElementChild
        tag_a.style.background = '';
        tag_a.style.width = '';
        tag_a.style.color = '';
    };
};