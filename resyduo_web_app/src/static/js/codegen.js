function statementContainerView(parentID, cardName) {
    var parent = document.getElementById(parentID)
    var card = document.createElement('div')
    card.className = "card bg-light mb-3"
    card.id = "variableDeclaration"
    card.innerHTML = '<div class="card-header"><h5>' + cardName + '</h5></div><div class="card-body" id="body"></div>'
    return card
}


function forViewGenerator(parentID) {
    var parent = document.getElementById(parentID)

}

function variableViewGenerator(parentID) {
    card = statementContainerView(parentID)
    var body = card.querySelector('#body')
    body.innerHTML = `<div class="row">
    <div class="col">
        <div class="input-group mb-3">
            <select class="form-select" id="inputGroupSelectLibrariesTab1">
                <option selected value="int">int</option>
                <option value="char">char</option>
                <option value="long">long</option>
                <option value="float">float</option>
                <option value="variable">double</option>
            </select>
            <label class="input-group-text" for="inputGroupSelectLibrariesTab1">Type</label>
        </div>
    </div>
    <div class="col">
        <div class="input-group mb-3">
            <input type="text" class="form-control" placeholder="x" aria-label="Variable"
                aria-describedby="basic-addon2">
            <div class="input-group-append">
                <span class="input-group-text" id="basic-addon2">id</span>
            </div>
        </div>
    </div>
    <div class="col">
        <div class="input-group mb-3">
            <input type="text" class="form-control" placeholder="0" aria-label="Variable"
                aria-describedby="basic-addon2">
            <div class="input-group-append">
                <span class="input-group-text" id="basic-addon2">Val
            </div>
        </div>
    </div>
</div>`
    card.appendChild(body)
    return card
}

function addStatementView(selectId, parentID) {

    var statement = document.getElementById(selectId).value;

    switch (statement) {
        case "variable":
            console.log(statement)
            variableView = variableViewGenerator(parentID)
            container = document.getElementById(parentID)
            container.appendChild(variableView)
            break;
        case "if":
            console.log(statement)
            break;
        case "for":
            console.log(statement)
            break;
        case "switch":
            console.log(statement)
            break;
    }
}

function generateCode(codeContainer) {
    console.log('generateCode(parentID):'+codeContainer)
    if (codeContainer.hasChildNodes()) {
        console.log('if child  hasChilds:')
        childs = codeContainer.childNodes
        console.log(childs.lenght)
        for (c in childs) {
            console.log('for child  id:'+c)
            if(c.id == "body")
            generateCode(c)
        }
    }
    else {
        console.log('ELSE child  id:'+childs[i])
        generateStatementCode(childs[i])
    }
}

function parseCodeSection(sectionId){
    codeContainer = document.getElementById(sectionId)
    generateCode(codeContainer)
}


function generateStatementCode(element) {
    statement = element.id
    switch (statement) {
        case "variableDeclaration":
            console.log('switch generate statement:' + statement)
            break;
        case "if":
            console.log('switch generate statement:' + statement)
            break;
        case "for":
            console.log('switch generate statement:' + statement)
            break;
        case "switch":
            console.log('switch generate statement:' + statement)
            break;
        default:
            console.log('switch DEFAULT statement:' + statement)
            break;
    }
}