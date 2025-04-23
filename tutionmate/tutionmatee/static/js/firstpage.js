
function load(){
    fetch('data')
    .then(res => res.json())
    .then(data => {
        data.teachers.forEach(teacher => {
        const yeet = document.getElementById("yeet")
        yeet.innerHTML +=` <div>  ${ teacher.name }</div> `

    })})}
