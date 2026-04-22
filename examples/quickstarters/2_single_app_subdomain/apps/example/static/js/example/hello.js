const button = document.getElementById('btnLoadApi');
const statusLabel = document.getElementById('apiStatus');
const responseBox = document.getElementById('apiResponse');

const setStatus = (text) => {
  statusLabel.textContent = text;
};

button.addEventListener('click', async () => {
  try {
    setStatus('Consultando endpoint REST...');
    responseBox.value = '';

    const response = await fetch(window.EXAMPLE_API_URL, {
      method: 'GET',
      headers: {
        Accept: 'application/json'
      }
    });

    const data = await response.json();
    responseBox.value = JSON.stringify(data, null, 2);

    if (!response.ok) {
      setStatus(`Error HTTP ${response.status}`);
      return;
    }

    setStatus('Respuesta recibida correctamente.');
  } catch (error) {
    setStatus('Fallo al consultar el endpoint REST.');
    responseBox.value = JSON.stringify({ error: String(error) }, null, 2);
  }
});
