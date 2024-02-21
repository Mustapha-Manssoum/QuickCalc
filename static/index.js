document.getElementById('calculatorForm').addEventListener('submit', async (event) => {
    event.preventDefault();  // prevent the default form submission

    // get values from the form
    const operand1 = encodeURIComponent(parseFloat(document.getElementById('operand1').value));
    const operation = encodeURIComponent(document.getElementById('operation').value);
    const operand2 = encodeURIComponent(parseFloat(document.getElementById('operand2').value));

    // Validate inputs
    if (isNaN(operand1) || isNaN(operand2)) {
        alert('Please enter a valid numbers');
        return;
    }

    // send data to the backend for processing
    try {
        const response = await fetch(`/calcul?operand1=${operand1}&operation=${operation}&operand2=${operand2}`, {
            method: 'GET',
            headers: {
                'Content-type': 'application/json',
            },
        });
    
        // check if the response is a valid json
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
    
        // display the result to the user
        console.log(data);
        document.getElementById('result').innerText = `Result: ${data}`;
    }
    
    catch(error) {
        console.error('Error:', error);
        alert('An error occurred. Check the console for details.');
    }
    
});