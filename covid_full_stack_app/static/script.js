 function getMeetings(){
          
            // The key javascript function here is fetch(), which is designed to get data from the backend. 
            // The code below is more readable than other examples you will find on the internet, but 
            // does the same thing. Borrowed from https://javascript.info/fetch

          fetch('/api/meetings/all')
            .then(
              // this is a magical feature of javascript called an "anonymous function" which is defined 
              // on the fly, without a name. 
              function(response) {
                // if the response is not a 200 OK (happy), "return", i.e. stop processing the data.
                if (response.status !== 200) {
                  // this is the equivalent to a python print() statement, and it will print to the browser console
                  console.log('Looks like there was a problem. Status Code: ' + response.status);
                  return;
                }
                          
                //if the response is a 200, check the data returned from the backend, in JSON format. 
                response.json().then(function(data) {
                  console.log(data);

                for (let i = 0; i < data.length; i++){
                  let paragraph = document.createElement('p');
                  paragraph.textContent = data[i];
                  document.body.appendChild(paragraph);
                }
                });
              }
            )
            .catch(function(err) {
              console.log('Fetch Error, booo!', err);
            });
        }