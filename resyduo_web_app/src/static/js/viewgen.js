function statementContainerView(parentID, cardName, stype, bodyId) {
    //var parent = document.getElementById(parentID)
    var card = document.createElement('div')
    card.className = "card bg-light mb-3"
    card.id = stype
    card.innerHTML = `
    <div class="card-header justify-content-between">
    <div class = "row">    
        <div class = "col">
                <h5>`+ cardName + `</h5>    
            </div>
            <div class = "col d-flex justify-content-end align-items-center">
                <span class="badge text-bg-secondary" onClick = "this.parentNode.parentNode.parentNode.parentNode.remove()">&#x2715</span>
            </div>
        </div>
    </div>
    <div class="card-body" id="`+ bodyId + `" stype="` + stype + `" parentCode ="`+parentID+`" >
    </div>
    `
    return card
}


function variableViewGenerator(parentID, statement) {
    bodyId = 'body' + Date.now()
    card = statementContainerView(parentID, statement, statement, bodyId)
    var body = card.querySelector('#' + bodyId)
    body.innerHTML = `
<div class="row">
    <div class="col">
        <div class="input-group mb-3">
            <select class="form-select" id="variableType">
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
                aria-describedby="basic-addon2" id="variableId" value ="x">
            <div class="input-group-append">
                <span class="input-group-text" id="basic-addon2">id</span>
            </div>
        </div>
    </div>
    <div class="col">
        <div class="input-group mb-3">
            <input type="text" class="form-control" placeholder="0" aria-label="Variable"
                aria-describedby="basic-addon2" id="variableValue"  >
            <div class="input-group-append">
                <span class="input-group-text" id="basic-addon2" >Val
            </div>
        </div>
    </div>
</div>
<div class = "row">
<div class="d-grid gap-2 d-md-flex justify-content-md-end">
    <button class="btn btn-primary btn-sm" type="submit"
        onclick="addStatementToCode('codeSection')">Add code</button>
</div>
</div>
`
    card.appendChild(body)
    return card
}



function forViewGenerator(parentID, statement) {
    bodyId = 'body' + Date.now()
    card = statementContainerView(parentID, statement, statement, bodyId)
    //console.log(card.innerHTML)
    var body = card.querySelector('#' + bodyId)
    //console.log('body', body, bodyId)
    selectUniqueId = Date.now()
    body.innerHTML = `
    <div class="row">
        <div class="col">
            <div class="row">
                <div class="col">
                <div class="input-group mb-3">
                <input type="text" class="form-control" placeholder="x" aria-label="Variable"
                    aria-describedby="basic-addon2" id="variableId" value ="x">
                <div class="input-group-append">
                    <span class="input-group-text" id="basic-addon2">from</span>
                </div>
            </div>
                </div>
                <div class="col">
                    <div class="input-group mb-3">
                        <input type="text" class="form-control" placeholder="x" aria-label="Variable"
                            aria-describedby="basic-addon2" id="forTo" value ="y.length">
                        <div class="input-group-append">
                            <span class="input-group-text" id="basic-addon2">to</span>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="input-group mb-3">
                        <input type="text" class="form-control" placeholder="0" aria-label="Variable"
                            aria-describedby="basic-addon2" id="forIncrement"  value ="i++">
                        <div class="input-group-append">
                            <span class="input-group-text" id="basic-addon2" >increment</div>
                    </div>
                </div>
            </div>
                <div class="row mt-3" hidden>
                    <h5>Nest Statement</h5>
                    <div class="input-group mb-3">
                        <select class="form-select" id="`+ selectUniqueId + `">
                            <option value = "for" >for</option>
                            <option value="switch" disabled>switch</option>
                            <option value="if" disabled>if</option>
                            <option value="method" disabled>method</option>
                            <option value="variable" selected>variable</option>
                        </select>
                        <label class="input-group-text" for="`+ selectUniqueId + `"
                            onclick="addStatementView(this.htmlFor,'`+ bodyId + `')">Add</label>
                    </div>
                </div>
        </div>
    </div>
    <div class = "row">
    <div class="d-grid gap-2 d-md-flex justify-content-md-end">
        <button class="btn btn-primary btn-sm" type="submit"
            onclick="addStatementToCode('codeSection')">Add code</button>
    </div>
    </div>
    `
    card.appendChild(body)
    return card
}

function addStatementView(selectId, parentID) {
    console.log("PARENT ID addStatementView", parentID)
    var statement = document.getElementById(selectId).value;
    container = document.getElementById(parentID)
    //console.log(container)
    switch (statement) {
        case "variable":
            variableView = variableViewGenerator(parentID, statement)
            container.appendChild(variableView)
            break;
        case "if":
            console.log(statement)
            break;
        case "for":
            console.log('switch case FOR')
            forView = forViewGenerator(parentID, statement)
            container.appendChild(forView)
            break;
        case "switch":
            console.log(statement)
            break;
    }
}