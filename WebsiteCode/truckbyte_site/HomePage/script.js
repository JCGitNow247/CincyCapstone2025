function Validate() {
  const SelectList = document.querySelector("select")
  const selectedValue = SelectList.value

  if(selectedValue == "") {
    return false
  } else {
    return true
  }
}

function SaveSelection() {
  const dropdown = document.getElementById("foodTruckDropdown");
  const selectedValue = dropdown.value;
  const selectedText = dropdown.options[dropdown.selectedIndex].text;

  // Save both value and text
  localStorage.setItem("selectedTruckValue", selectedValue);
  localStorage.setItem("selectedTruckName", selectedText);
}

function OrderNow() {
  
  let OrderValidation = Validate()

  if(OrderValidation == true) {
    SaveSelection();
    window.location.href = "../OrderPage/OrderPage.html"
  } 
  else {
    console.log("Please Select a Location")
  }
}