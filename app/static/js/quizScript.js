
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
    var answers = ["a", "b", "c", "d", "a"];

    // Check Answers
    for (i = 1; i <= total; i++){
        if (eval("q" + i) == answers[i-1]){
            var wes = document.getElementById("q"+i+"h");
            wes.classList.add("correct");
            score++;
        }
        if(eval("q" + i) != answers[i-1]) { 
            var wes = document.getElementById("q"+i+"h");
            wes.classList.add("wrong");
            let correction = document.getElementById(i+"results");
            correction.innerHTML = "<h3>You selected <span>" + eval("q" + i) + "</span>. The correct answer was <span>" + answers[i-1] +"</span></h3>" 
        }
    }

    // Display Results
    let results = document.getElementById("results");
    results.innerHTML = "<h3>You scored <span>" + score+ "</span> out of <span>" + total + "</span></h3>"

    // alert("You scored " + score + " out of " + total);
    var fileName = location.href.split("/").slice(-1);
    var fileName = location.href.slice(0, -5) 
    let precentage = (score/total)*100;
    let r = document.getElementById("return");
    r.innerHTML = "<form action=\"{{ url_for('handle_quiz', quizname='" + "Demand and Supply"
    + "', quizurl='"+ fileName +"', quiz_scoreoutofhundred=" + precentage +") }}\"> <input type=\"submit\" value=\"Return\"> </form>"


    return false;
}

function send_score() {
    var id = location.href.split("/").slice(-1);
    var id = location.href.slice(0, -5)  
    var filename = "Demand and Supply";
    var url = "handle_quiz/"+ filename +"/"+ id +"/"+ score/total*100;
    var data = score/total*100;
    $.post(url, data);
    return false;
}