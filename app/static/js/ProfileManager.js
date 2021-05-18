function submitProfile(){
    var x = document.getElementById("myFile");
    var txt = "";
    console.log("started");
    if ('files' in x) {
      if (x.files.length == 0) {
        txt = "Select a Picture";
      } else {
        img.src = URL.createObjectURL(this.x[0]);
        console.log(img.src);
        document.getElementById ("pic").innerHTML = "<img src='"+img.src+"url' alt='alternatetext'>"
      }
    } 
    else {
      if (x.value == "") {
        txt += "Select one or more files.";
      } else {
        txt += "This format is not supported by your browser!";
        txt  += "<br>The path of the selected file: " + x.value; // If the browser does not support the files property, it will return the path of the selected file instead. 
      }
    }
    document.getElementById("aboutPicture").innerHTML = txt;
}