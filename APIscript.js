let p = fetch("http://127.0.0.1:5500/index.html")
p.then((response) =>{
       console.log(response.status)
       console.log(response.ok)
       console.log(response.headers)
       return response.json()
}).then((value2) => {
    console.log(value2)
})