
function load(){
    fetch('data')
    .then(res => res.json())
    .then( data => {
        data.teachers.forEach( teacher  => {
            console.log(teacher.name)
        })
    })
}