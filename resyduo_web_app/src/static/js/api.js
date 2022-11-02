
/*

Tag Api Functions

*/

function getAllTag(data){
    return fetch('/api/tag/', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
        })
        .then(response => response.json())
        .catch((error) => {
        console.error('Error:', error);
        });
    }



function getComponentsByTags(data){
    return fetch('/api/search/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
        })
        .catch((error) => {
        console.error('Error:', error);
        });
    }


/*

Tag Component Functions

*/

function getAllTag(data){
    return fetch('/api/component/', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
        })
        .then(response => response.json())
        .catch((error) => {
        console.error('Error:', error);
        });
    }

function getLibsByComponents(data){
    return fetch('/api/search/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
        })
        .catch((error) => {
        console.error('Error:', error);
        });
    }