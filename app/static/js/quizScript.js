function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  
function submitAnswers(){
    let total = 5;
    let score = 0;

    // Get user input
    let q1 = document.forms["quizForm"]["q1"].value;
    let q2 = document.forms["quizForm"]["q2"].value;
    let q3 = document.forms["quizForm"]["q3"].value;
    let q4 = document.forms["quizForm"]["q4"].value;
    let q5 = document.forms["quizForm"]["q5"].value;

    // Validation
    if (q1 == null || q1 == ""){
        alert("You missed question 1");
        return false;
    }

    for (i = 1; i <= total; i++){
        // Use eval to concat string q with value of i to get var q1, q2, etc
        if (eval("q" + i) == null || eval("q" + i) == ""){
            alert("You missed question " + i);
            return false;
        }
    }

    // Set Correct Answers
    var answers = [];
    var id = location.href.split("/").slice(-1);
    console.log(id);
    if(id == "ds_quiz"){
        var answers = ["b", "c", "c", "b", "c"];
    }
    if(id == "elasticity_quiz"){
        var answers = ["c", "a", "a", "c", "a"];
    }
    if(id == "surplus_quiz"){
        var answers = ["a", "c", "b", "c", "c"];
    }
    // Check Answers
    for (i = 1; i <= total; i++){
        if (eval("q" + i) == answers[i-1]){
            var wes = document.getElementById("q"+i+"h");
            let correction = document.getElementById(i+"results");
            correction.innerHTML = "<h3>You selected <span>" + eval("q" + i) + "</span>. The correct answer was <span>" + answers[i-1] +"</span></h3>" 
            correction.classList.add("correct");
            score++;
        }
        if(eval("q" + i) != answers[i-1]) { 
            var wes = document.getElementById("q"+i+"h");
            let correction = document.getElementById(i+"results");
            correction.innerHTML = "<h3>You selected <span>" + eval("q" + i) + "</span>. The correct answer was <span>" + answers[i-1] +"</span></h3>" 
            correction.classList.add("wrong");
        }
        // Display Results
        let results = document.getElementById("results");
        results.innerHTML = "<h3>You scored <span>" + score+ "</span> out of <span>" + total + "</span></h3>"

    }
}
