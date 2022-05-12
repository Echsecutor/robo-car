
async function reboot(){
    alert("rebooting");
    let out = document.getElementById('out_terminal');
    let response = await fetch("/reboot");
    let response_body = await response.text();
    out.innerHTML = response_body;
}
