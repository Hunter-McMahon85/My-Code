/*
  Name: Hunter McMahon
  Class: CIS 111
  Description: <lab 08 js file, man 2008 was better than now tbh, then again i was 6 with no wories then>
*/

function handleAddListItemButton(evt) {
  console.log("handle Add List Item Button pushed");

  //get data from input
  const data = document.querySelector('#coffeeInput').value.trim();

  //add data to list
  let listitem = document.createElement("li")

  //set the input stored as data as the content of the LI
  listitem.textContent = data;

  //add the Li to the ordered list
  if (data.length > 0) {
    document.querySelector("ol").appendChild(listitem)
  }

};

function handleChangeListTypeButton(evt) {
  console.log("handle Change List typem Button pushed");

  //determine list type 
  let listtype = document.querySelector("#listTypeInput").value.trim();
  //set list type 
  if (listtype === "1" || listtype === "A" || listtype === "a" || listtype === "I" || listtype === "i") {
    document.querySelector("ol").setAttribute("type", listtype);
  }
};

function handleRemoveLastListItemButton(evt) {
  console.log("handle remove last List Item Button pushed");
  // finding last item
  let disownedchild = document.querySelector('ol li:last-child');

  //killing the last item for its crimes against humanity
  if (disownedchild != undefined) {
    document.querySelector("ol").removeChild(disownedchild);
  }
};

//detecting user input (pushing buttons) & calling needed function

document.querySelector('#addListItemButton').addEventListener('click', handleAddListItemButton);
document.querySelector('#changeListTypeButton').addEventListener('click', handleChangeListTypeButton);
document.querySelector('#removeLastListItemButton').addEventListener('click', handleRemoveLastListItemButton);

//document.querySelector('html element id/class identifier').addEventListener('event', function);