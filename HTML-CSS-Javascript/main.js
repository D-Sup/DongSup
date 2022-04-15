let targot = document.querySelector("#dynamic");

function randomString(){
    let stringArr = ["Learn to HTML", "Learn to CSS",
    "Learn to Javascript", "Learn to Python", "Learn to Ruby"];
    let selectString = stringArr[Math.floor(Math.random() * stringArr.length)];
    let selectStringArr = selectString.split("");

    return selectStringArr;
}

//타이핑 리셋
function resetTyping(){
    targot.textContent = "";
    dynamic(randomString());
}

//한글자씩 테스트 출력함수
function dynamic(randomArr){
    if(randomArr.length > 0){
        targot.textContent += randomArr.shift();
        setTimeout(function(){
            dynamic(randomArr);
        }, 80);
    }else{
        setTimeout(resetTyping, 3000);
    }
}

dynamic(randomString());

//커서 깜빡임 효과
function blink(){
    targot.classList.toggle("active");
}
setInterval(blink, 500);

