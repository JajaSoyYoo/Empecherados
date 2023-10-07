document.addEventListener('DOMContentLoaded', function () {
    const trabajoInput = document.getElementById('trabajoInput');
    const sectorInput = document.getElementById('sectorInput');
    const camposNA = document.querySelectorAll('[data-na]');

    trabajoInput.addEventListener('change', function () {
        if (this.value === 'No') {
            camposNA.forEach(function (campo) {
                if (campo.tagName === 'SELECT') {
                    // Si es un campo de selección, selecciona la opción "N/A" y deshabilita el campo
                    campo.value = 'NoAplica';
                    campo.disabled = true;
                } else {
                    // Establece el valor en "N/A" y deshabilita el campo
                    campo.value = 'N/A';
                    campo.disabled = true;
                }
            });
        } else {
            camposNA.forEach(function (campo) {
                if (campo.tagName === 'SELECT') {
                    // Si es un campo de selección, selecciona la primera opción y habilita el campo
                    campo.selectedIndex = 0;
                    campo.disabled = false;
                } else {
                    // Establece el valor en blanco y habilita el campo
                    campo.value = '';
                    campo.disabled = false;
                }
            });
        }
    });
});
