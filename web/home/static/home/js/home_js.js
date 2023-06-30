const url = window.location.href
const serachForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const resultsBox = document.getElementById('results-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value

const sendSearchDeta = (product) => {
    $.ajax({
        type : 'POST',
        url : 'search/',
        data : {
            'csrfmiddlewaretoken' : csrf,
            'product' :product,

        },
        success : (res)=> {
            console.log(res.data)
            const data = res.data
            if(Array.isArray(data)){
                resultsBox.innerHTML = ''
                data.forEach(product => {
                    resultsBox.innerHTML +=  `
                        <a href='detail/${product.slug}' class="item">
                            <div class="row mt-2 mb-2">
                                <div class= "col-2">
                                    <img src="${product.image}">
                                </div>
                                <div class= "col-10">
                                    <h5>${product.name}</h5>
                                </div>
                            </div>
                        </a>
                    
                    `                
                    
                })
            } else{
                if (searchInput.value.length > 0) {
                    resultsBox.innerHTML = `<b>${data}</b>`
                } else {
                    resultsBox.classList.add('not-visible')
                }
            }

        },

        error : (err) => {
            console.log(err)

        }


    })

}

searchInput.addEventListener('keyup' , e=>{
    console.log(e.target.value)


    if (resultsBox.classList.contains('not-visible')){
        resultsBox.classList.remove('not-visible')
    }
    

    sendSearchDeta(e.target.value)

})