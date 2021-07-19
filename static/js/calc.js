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
    p.innerHTML = Number(e.target.dataset.price) * Number(e.target.value)
    const finalpri = document.getElementById('finalprice')
    let total = 0
    let prices = document.querySelectorAll(".priceform")
    prices.forEach((elem) => {
        total += Number(elem.innerHTML)
    })
    finalpri.innerHTML = total

}


const countProducts = async (e, p, countinfirmer) => {
    console.log(e.path[0].options[e.path[0].options.selectedIndex].dataset.pricetext)
    countinfirmer.innerHTML = e.path[0].options[e.path[0].options.selectedIndex].dataset.pricetext
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
    category.className = 'form-select catform'
    wrapper.appendChild(category)
    let product = document.createElement("select");
    product.className = 'form-select prodform'
    // product.setAttribute('disabled',true)
    wrapper.appendChild(product)
    let countinfirmer = document.createElement("div");
    countinfirmer.className = 'countformlabel'
    countinfirmer.innerHTML = 'Количество'
    wrapper.appendChild(countinfirmer)
    let count = document.createElement("input");
    count.className = 'form-control countform'
    // count.setAttribute('disabled',true)
    wrapper.appendChild(count)
    let price = document.createElement("div");
    price.className = 'priceform'
    price.innerHTML = '0'
    wrapper.appendChild(price)
    product.onchange = (e) => countProducts(e, count, countinfirmer)
    category.onchange = (e) => products(e, product)
    count.onfocus = (e) => count.value = ''
    count.oninput = (e) => productPrice(e, price)

    wrapper.style.opacity = 0;

    wrapper.style.transition = '0.2s';
    wrapper.style.transform = 'scale(0)'


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


    window.setTimeout(function () {
        wrapper.style.opacity = 1;
        wrapper.style.transform = 'scale(1)'

    }, 10)
    item.insertBefore(wrapper, item.firstChild);

}

const senddata = () =>{
    let data = document.querySelectorAll(".calcItemGroup")
    console.log(data)
}
document.addEventListener("DOMContentLoaded", addNewProduct);