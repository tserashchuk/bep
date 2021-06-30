const getCats = async () => {
    let response = await fetch('/api-auth/category/', {method: 'GET'})
    let data = await response.json()
    return data
}

const getProds = async (category) => {
    let response = await fetch(`/api-auth/products/?category_id=${category}`, {method: 'GET'})
    let data = await response.json()
    return data
}

const finalpri = document.getElementById('finalprice')

// =====================================================================================================================

const productPrice = (e, p) => {
    p.value = Number(e.target.dataset.price) * Number(e.target.value)
    const finalpri = document.getElementById('finalprice')
    let total = 0
    let prices = document.querySelectorAll(".price")
    prices.forEach((elem) => {
        total += Number(elem.value)
    })
    finalpri.innerHTML = total

}


const countProducts = async (e, p) => {
    console.log(e.path[0].options[e.path[0].options.selectedIndex].dataset.pricetext)
    p.value = 'Сколько' + ' ' + e.path[0].options[e.path[0].options.selectedIndex].dataset.pricetext + ' вы хотите сдать?'
    p.setAttribute('data-price', e.target.value)
}


const products = async (e, product) => {
    let data = await getProds(e.target.value)
    product.innerHTML = ''
    let bufoption = document.createElement("option");
    bufoption.text = 'Выберите продукт'
    product.appendChild(bufoption);
    for (dat of data) {
        let option = document.createElement("option");
        option.value = dat['product_price'];
        option.text = dat['product_name'];
        option.setAttribute('data-pricetext', dat['color'])
        product.appendChild(option);
    }

}

const createWrapper = () => {
    let wrapper = document.createElement('div')
    wrapper.className = 'form-row calcItemGroup'
    let category = document.createElement("select");
    category.className = 'form-select'
    wrapper.appendChild(category)
    let product = document.createElement("select");
    product.className = 'form-select'
    // product.setAttribute('disabled',true)
    wrapper.appendChild(product)
    let count = document.createElement("input");
    count.className = 'form-control'
    // count.setAttribute('disabled',true)
    wrapper.appendChild(count)
    let price = document.createElement("input");
    price.className = 'form-control price'
    wrapper.appendChild(price)
    product.onchange = (e) => countProducts(e, count)
    category.onchange = (e) => products(e, product)
    count.onfocus = (e) => count.value = ''
    count.oninput = (e) => productPrice(e, price)

    return [category, wrapper]
}

const addNewProduct = async () => {

    let [category, wrapper] = createWrapper()

    let item = document.getElementById("calcForm");
    let data = await getCats()
    let bufoption = document.createElement("option");
    bufoption.text = 'Выберите категорию'
    category.appendChild(bufoption);
    for (dat of data) {

        let option = document.createElement("option");
        option.value = dat['id'];
        option.text = dat['cat_name'];
        category.appendChild(option);
    }

    // item.appendChild(wrapper)
    item.insertBefore(wrapper, item.firstChild);

}


document.addEventListener("DOMContentLoaded", addNewProduct);