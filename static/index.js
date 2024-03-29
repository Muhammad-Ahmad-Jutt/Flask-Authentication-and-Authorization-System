//calling the SignIn api
function signIn() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    console.log(username+password)
    fetch('/login', {
        method : 'POST',
        headers : {
            'Content-Type': 'application/json'
        },
        body : JSON.stringify({username: username, password: password})
    })
    .then(response => response.json())
    .then(data => {
        var tokenInfoString = JSON.stringify(data);
        document.getElementById('signedInuser').innerHTML = ' Token generated'
        localStorage.setItem('tokenInfo', tokenInfoString);
        console.log('Token info saved to local storage.');
        fetchUserInfo(token);
        
    })
}
//Calling the check status api
function check_status() {
    var tokenInfoString = localStorage.getItem('tokenInfo');
    if (tokenInfoString) {
        try {
            // Parse stringified JSON data back to JSON object
            var retrievedTokenInfo = JSON.parse(tokenInfoString);
            // Extract token from tokenInfo
            var token = retrievedTokenInfo.token;

            // Log the retrieved token info
            
            fetch('/items', {
                method : 'GET',
                headers : {
                    'Authorization': 'Bearer ' + token,
                    'Content-Type': 'application/json'
                },
            })
            
            .then(data => {
                fetchUserInfo(token)
                // Handle the response data here
            })
            .catch(error => {
                document.getElementById('signedInuser').innerHTML = error;
                // Handle errors here
            });
        } catch (error) {
            document.getElementById('signedInuser').innerHTML = error;
            // Handle errors here
        }
    } else {
        document.getElementById('signedInuser').innerHTML = 'No token info found in local storage.'
        // Handle the case when token info is not found in local storage
    }
}
//calling the fetch info api
function fetchUserInfo(token) {
    fetch('/user_info', {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Display user's name
        document.getElementById('signedInuser').innerText = "Signed in as: " + data.username;
    })
    .catch(error => {
        console.error('Error fetching user info:', error);
    });
}

//calling the logout api 
function logout() {
    var tokenInfoString = localStorage.getItem('tokenInfo');
    if (tokenInfoString) {
        try {
            // Parse stringified JSON data back to JSON object
            var retrievedTokenInfo = JSON.parse(tokenInfoString);
            // Extract token from tokenInfo
            var token = retrievedTokenInfo.token;

            // Log the retrieved token info

            fetch('/logout', {
                method: 'POST',
                headers: {
                    Authorization: 'Bearer ' + token,
                    'Content-Type': 'application/json'
                }
            })
            .then(response => {
                document.getElementById('signedInuser').innerHTML = 'token_removed from the data'
                localStorage.removeItem('tokenInfo');
            })
            .catch(error => {
                console.error('Error:', error);
                // Handle errors here
            });
        } catch (error) {
            console.error('Error parsing JSON:', error);
            // Handle errors here
        }
    } else {
        document.getElementById('signedInuser').innerHTML = 'No token found'
        // Handle the case when token info is not found in local storage
    }
}
