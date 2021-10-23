var obj_csv = {
  size: 0,
  dataFile: []
};

function readImage(input) {
  if (input.files && input.files[0]) {
    let reader = new FileReader();
    reader.readAsBinaryString(input.files[0]);
    reader.onload = function (e) {
      console.log(e);
      obj_csv.size = e.total;
      obj_csv.dataFile = e.target.result
      console.log(obj_csv.dataFile)
      return (parseData(obj_csv.dataFile))
    }
  }
}

function parseData(data) {
  let csvData = [];
  let lbreak = data.split("\n");
  lbreak.forEach(res => {
    csvData.push(res.split(","));
  });
  return csvData;
}
data = [7][7]
data[3][3] = readImage('analysis.csv')
console.log(data[2][2])

const charts = document.querySelectorAll(".chart");

charts.forEach(function (chart) {
  var ctx = chart.getContext("2d");
  var myChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["KNN-3", "KNN-5", "KNN-7", "Decision Tree", "Naive Bayes", "SVM", "Random Forest"],
      datasets: [
        {
          label: ["Accuracy"],
          data: [87, 88, 57, 43.65, 93, 12, 12],
          backgroundColor: [
            "rgba(54, 200, 235, .11)",
          ],
          borderColor: [
            "rgba(54, 162, 235, 1)",
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
});

$(document).ready(function () {
  $(".data-table").each(function (_, table) {
    $(table).DataTable();
  });
});


(function () {
  'use strict'
  const forms = document.querySelectorAll('.requires-validation')
  Array.from(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
})()


//selecting all required elements
const dropArea = document.querySelector(".drag-area"),
  dragText = dropArea.querySelector("header"),
  button = dropArea.querySelector("button"),
  input = dropArea.querySelector("input");
let file; //this is a global variable and we'll use it inside multiple functions

button.onclick = () => {
  input.click(); //if user click on the button then the input also clicked
}

input.addEventListener("change", function () {
  //getting user select file and [0] this means if user select multiple files then we'll select only the first one
  file = this.files[0];
  dropArea.classList.add("active");
  showFile(); //calling function
});


//If user Drag File Over DropArea
dropArea.addEventListener("dragover", (event) => {
  event.preventDefault(); //preventing from default behaviour
  dropArea.classList.add("active");
  dragText.textContent = "Release to Upload File";
});

//If user leave dragged File from DropArea
dropArea.addEventListener("dragleave", () => {
  dropArea.classList.remove("active");
  dragText.textContent = "Drag & Drop to Upload File";
});

//If user drop File on DropArea
dropArea.addEventListener("drop", (event) => {
  event.preventDefault(); //preventing from default behaviour
  //getting user select file and [0] this means if user select multiple files then we'll select only the first one
  file = event.dataTransfer.files[0];
  showFile(); //calling function
});

function showFile() {
  let fileType = file.type; //getting selected file type
  let validExtensions = ["csv"]; //adding some valid image extensions in array
  if (validExtensions.includes(fileType)) { //if user selected file is an image file
    let fileReader = new FileReader(); //creating new FileReader object
    fileReader.onload = () => {
      let fileURL = fileReader.result; //passing user file source in fileURL variable
      // UNCOMMENT THIS BELOW LINE. I GOT AN ERROR WHILE UPLOADING THIS POST SO I COMMENTED IT
      // let imgTag = `<img src="${fileURL}" alt="image">`; //creating an img tag and passing user selected file source inside src attribute
      dropArea.innerHTML = imgTag; //adding that created img tag inside dropArea container
    }
    fileReader.readAsDataURL(file);
  } else {
    alert("This is not an CSV File!");
    dropArea.classList.remove("active");
    dragText.textContent = "Drag & Drop to Upload File";
  }
}
