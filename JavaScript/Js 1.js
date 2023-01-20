// Cashing the DOM
// Cache means storing something for future use

var userScore = 0;
var compScore = 0;
const userScore_span = document.getElementById("user-score");
const compScore_span = document.getElementById("comp-score");
const scoreboard_div = document.querySelector(".scoreboard");
const result_p = document.querySelector(".result > p");
const rock_div = document.getElementById('rock');
const paper_div = document.getElementById('paper');
const scissors_div = document.getElementById('scissors')

function getCompChoice(){
  const choices = [null, "rock", "paper", "scissors"];
  const random = Math.floor((Math.random()*3) +1);
  // console.log("Computer choce " + choices[random]);
  return choices[random];
}

function win(user, comp){
  console.log("User Wins");
  userScore++;
  userScore_span.innerHTML = userScore;
  result_p.innerHTML = "(User) ".sub().fontsize(3) + user + " VS " + comp + " You Win" + " (Comp)".sub().fontsize(3);
  document.getElementById(user).classList.add("win-glow");
  setTimeout(function() { document.getElementById(user).classList.remove("win-glow")}, 600);
}

function draw(user, comp){
  console.log("It is a draw");
  result_p.innerHTML = "(User) ".sub().fontsize(3) + user + " and " + comp + " is a Draw" + " (Comp)".sub().fontsize(3);
  document.getElementById(user).classList.add("draw-glow");
  setTimeout(function() { document.getElementById(user).classList.remove("draw-glow")}, 600);
}
function lost(user, comp){
  console.log("Computer Wins");
  compScore++;
  compScore_span.innerHTML = compScore;
  result_p.innerHTML = "(User) ".sub().fontsize(3) + user + " VS " + comp + " you Lose" + " (Comp)".sub().fontsize(3);
  document.getElementById(user).classList.add("loose-glow");
  setTimeout(function() { document.getElementById(user).classList.remove("loose-glow")}, 600);
}

function game(userChoice) {
  const compChoice = getCompChoice();
  console.log(userChoice, " VS ", compChoice);
  switch (userChoice + " VS " + compChoice) {
    case "rock VS scissors":
    case "paper VS rock":
    case "scissors VS paper":
      win(userChoice, compChoice);
      break;
    case "rock VS rock":
    case "paper VS paper":
    case "scissors VS scissors":
      draw(userChoice, compChoice);
      break;
    default:
      lost(userChoice, compChoice);
  }
}

function main(){
  rock_div.addEventListener('click',
  function() {
  game("rock");
  })
  paper_div.addEventListener('click',
  function() {
  game("paper");
  })
  scissors_div.addEventListener('click',
  function() {
  game("scissors");
  })}

main()
