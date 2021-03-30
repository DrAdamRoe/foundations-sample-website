function getMeetings() {
  // The key javascript function here is fetch(), which is designed to get data from the backend.
  // The code below is more readable than other examples you will find on the internet, but
  // does the same thing. Borrowed from https://javascript.info/fetch

  fetch("/api/meetings/all")
    .then(
      // this is a magical feature of javascript called an "anonymous function" which is defined
      // on the fly, without a name.
      function (response) {
        // if the response is not a 200 OK (happy), "return", i.e. stop processing the data.
        if (response.status !== 200) {
          // this is the equivalent to a python print() statement, and it will print to the browser console
          console.log(
            "Looks like there was a problem. Status Code: " + response.status
          );
          return;
        }

        // if the response is a 200, check the data returned from the backend isin JSON format.
        // if that passes, print the data to the javascript console on the browser.
        response.json().then(function (data) {
          console.log(data);

          // Your Homework: instead of printoing to the cosnole, change what the user sees.
        });
      }
    )
    .catch(function (err) {
      console.log("Fetch Error, booo!", err);
    });
}

function createNewMeeting() {
  // creates a new javascript object called form_data, of the type FormData, based on the contents
  // of a form called meeting-form, which is the form defined in index.html.
  const form_data = new FormData(document.getElementById("meeting-form"));
  fetch("/api/meetings", {
    method: "POST",
    body: form_data,
  })
    .then(
      //same basic code as above - catch errors if there are any.
      function (response) {
        // if the response is not a 201 OK (resource created), log it.
        if (response.status !== 201) {
          // this is the equivalent to a python print() statement, and it will print to the browser console
          console.log(
            "Looks like there was a problem. Status Code: " + response.status
          );
        }
      }
    )
    .catch(function (err) {
      console.log("Fetch Error, booo!", err);
    });
}
