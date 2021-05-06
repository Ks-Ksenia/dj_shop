function findPointMainMenu(event, class_menu){
    let target = event.target;
    let parentTarget = target.closest(class_menu);

    let tagA = parentTarget.firstElementChild
    return tagA
};

function styleOnMouseOver(event, class_menu){
    let tagA = findPointMainMenu(event, class_menu)

    tagA.style.background = '#6d068f';
    tagA.style.width = '91%';
    tagA.style.color = '#fff';
};

function styleOnMouseOut(event, class_menu){
    let tagA = findPointMainMenu(event, class_menu)

    tagA.style.background = '';
    tagA.style.width = '';
    tagA.style.color = '';
};

let menu = document.querySelectorAll('.menu');

for (let pointMenu of menu){
    pointMenu.onmouseover = function(event){

        if (document.querySelector('.hidden_topmenu')){
            let class_menu = '.hidden_topmenu'
            styleOnMouseOver(event, class_menu)

        }
        if (document.querySelector('.topmenu')){
            let class_menu = '.topmenu'
            styleOnMouseOver(event, class_menu)

            }

    };

    pointMenu.onmouseout = function(event){

        if (document.querySelector('.hidden_topmenu')){
            let class_menu = '.hidden_topmenu'
            styleOnMouseOut(event, class_menu)
        };
        if (document.querySelector('.topmenu')){
            let class_menu = '.topmenu'
            styleOnMouseOut(event, class_menu)
        };


    };
};