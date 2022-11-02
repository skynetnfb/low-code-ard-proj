function generate_recommended_components(){
    console.log("generate_recommended_components()")

    tab1_components_section = document.getElementById("tab1-components-section")
    tab1_select_components = document.getElementById("tab1-select-components")

    console.log(tab1_select_components.className)
    console.log(tab1_components_section.className)
    components = ["componente1","componente2"]
    for (i=0; i < components.length; i += 1) {
        option = document.createElement('option');
        option.setAttribute('value', i);
        option.appendChild(document.createTextNode(components[i]));
        tab1_select_components.appendChild(option);
    }
    tab1_components_section.className = "row mt-3"
}

