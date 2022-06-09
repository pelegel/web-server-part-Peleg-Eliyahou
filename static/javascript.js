/*pull the pathname of the active page from window location.
put an "active" class to the active page by creating an array of the nav's links and comparing
each path name to the currently active page*/
const activePage = window.location.pathname;
const navLinks = document.querySelectorAll('nav a').forEach(link => {    
  if(link.href.includes(`${activePage}`)){
    link.classList.add('active');
  }
});


//calculate and print the average time the user listen to music according to it's input
function calcTime() {
  const numOfSongs = document.getElementById("inputNum").value;
  var res = "you listen to songs for an average time of ";
  res += numOfSongs*3.5;
  res += " minutes a day";
  document.getElementById("result").innerHTML = res;
}


//ask the user to get promotion if didn't agree. if doesn't want promotions again - submiting the form
var times = 0;
var contact = 0;
function submitForm() {

  if (agree.checked == false && times ==0){
    window.alert("Are you sure you don't want to get promotion emails?"); 
    times+=1; 
  } 
  else if (times==1){
    window.alert("Thank you for contacting us!");  
    times +=1;
    contact = 1;
  }
  else if (agree.checked == true && contact ==0){
    window.alert("Thank you for contacting us!");  
    contact = 1;
  }
  else{
    window.alert("You have already submited the form");  
  } 

}

