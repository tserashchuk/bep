const getCats = async () => {
    let response = await fetch('/api-auth/category/', {method: 'GET'})
    let data = await response.json()
    return data
}

const getProds = async () => {
    let response = await fetch(`/api-auth/products/`, {method: 'GET'})
    let data = await response.json()
    return data
}



const find = async (query) => {
    let products = await getProds();
    if (query.length>=3) {
    let searchResults =  products.filter((element)=>{
        return element['product_name'].match(query.value)
    })}
    let pr = document.getElementById('productansw')
    pr.innerHTML = ''
    for (let element of searchResults) {

        pr.innerHTML += element['product_name']
        pr.innerHTML += '</br>'
    }
}