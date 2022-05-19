function terminal_add (text) {
  let out = document.getElementById('out_terminal')
  out.innerHTML = out.innerHTML + text + '\n'
  out.scrollTop = out.scrollHeight
}

async function set_motor (position, side, action) {
  terminal_add('setting motor ' + position + ' ' + side + ' to ' + action)
  let response_body = await post_and_get_response('/set_motor', {"position" : position, "side": side, "action": action})
  terminal_add(response_body)
}

async function reboot () {
  if (window.confirm('Really reboot?')) {
    terminal_add('Sending reboot command...')
    let response_body = await get_response_body('/reboot')
    terminal_add(response_body)
  }
}

async function poweroff () {
    if (window.confirm('Really Shut Down?')) {
      terminal_add('Sending shutdown command...')
      let response_body = await get_response_body('/poweroff')
      terminal_add(response_body)
    }
  }

async function get_response_body (url) {
  let response = await fetch(url)
  return await response.text()
}

async function post_and_get_response (url, body_object) {
  const opts = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(body_object)
  }
  let response = await fetch(url, opts)
  return await response.text()
}

async function load_banner () {
  let response_body = await get_response_body('/static/banner.txt')
  terminal_add(response_body)
}
