document.getElementById("weather-form").addEventListener("submit", async (event) => {
    event.preventDefault();
    const city = document.getElementById("city").value;

    try {
        const response = await fetch("/weather", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ city })
        });

        if (response.ok) {
            const data = await response.json();
            document.getElementById("result").innerHTML = `
                <p><strong>City:</strong> ${data.city}</p>
                <p><strong>Temperature:</strong> ${data.temperature}°F</p> 
                <p><strong>Description:</strong> ${data.description}</p>
                <p><strong>Humidity:</strong> ${data.humidity}%</p>
                <p><strong>Wind Speed:</strong> ${data.wind_speed} mph</p> 
            `;
        } else {
            const error = await response.json();
            document.getElementById("result").innerHTML = `<p>Error: ${error.detail}</p>`;
        }
    } catch (error) {
        document.getElementById("result").innerHTML = `<p>Something went wrong: ${error.message}</p>`;
    }
});
