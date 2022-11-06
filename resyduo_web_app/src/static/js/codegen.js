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
</div>`
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
                <div class="row mt-3">
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


function parseCodeSection(sectionId) {
    codeContainer = document.getElementById(sectionId)
    tree = getTreeCode(codeContainer)
    tree = visitTree(tree, generateStatementCode)
    console.log("tree with code:", tree )
}

function visitTree(tree,fn){
    for(i=0; i < tree.length; i++){
        if(tree[i].children.length>0){
            console.log(tree[i].children)
            visitTree(tree[i].children,(f)=>{})
        }
        else{
            fn(tree, tree[i],'codeSection')
        }
    }
    return tree
}



function getTreeCode(codeContainer) {
    codeArr=[]
    let list = []
    codeArr = walkDom2(codeContainer, 'card-body');
    for (i = 0; i < codeArr.length; i++){
        obj = {}
        obj ["id"] = codeArr[i].id
        obj ["parentId"] = codeArr[i].getAttribute("parentCode")
        obj ["statement"] = codeArr[i].getAttribute("stype")
        obj ["bodyCode"] = ""
        list.push(obj)  
    }
    tree = list_to_tree(list, 'codeSection')
    return tree
}

function list_to_tree(list,root) {
    var map = {}, node, roots = [], i;
    
    for (i = 0; i < list.length; i += 1) {
      map[list[i].id] = i; // initialize the map
      list[i].children = []; // initialize the children
    }
    //console.log('list: ',list)
    //console.log('map: ',map)
    for (i = 0; i < list.length; i += 1) {
      node = list[i];
      if (node.parentId !== root) {
        // if you have dangling branches check that map[node.parentId] exists
        list[map[node.parentId]].children.push(node);
      } else {
        roots.push(node);
      }
    }
    //console.log(roots)
    return roots;
  }


function walkDom2(start_element, filterClass) {
    var arr = []; // put all elements here
    var loop = function (element) {
        
        do {
            // we can do something with element
            if (element.nodeType == 1) { // do not include text nodes
                if (element.className == filterClass) {
                    arr.push(element);
                }
            }
            if (element.hasChildNodes())
                loop(element.firstChild);
        }
        while (element = element.nextSibling);
    }
    
    //loop(start_element);
    loop(start_element.firstChild); // do not include siblings of start element
    return arr;
}

walkDom(document.body);



function generateStatementCode(tree, item, root) {
    console.log('generateStatementCode()')
    statement = item.statement
    switch (statement) {
        case "variable":
            console.log('switch generate statement:' + statement)
            item.bodyCode = "variable code"
            if(item.parentId =! root){

            }
            //getVariableDeclarationCode(id_element)
            break;
        case "if":
            console.log('switch generate statement:' + statement)
            break;
        case "for":
            console.log('switch generate statement:' + statement)
            item.bodyCode = "for body code"
            break;
        case "switch":
            console.log('switch generate statement:' + statement)
            break;
        default:
            console.log('switch DEFAULT statement:' + statement)
            break;
    }
}

function getVariableDeclarationCode(element) {
    //console.log('getVariableDeclarationCode(element) class:' + element.className)
    variableType = element.querySelector('#variableType')
    variableId = element.querySelector('#variableId')
    variableValue = element.querySelector('#variableValue')
    code = variableType.value + ' ' + variableId.value + ' ' + '=' + ' ' + variableValue.value + ';'
    console.log('code' + code)
}

function getForCode() {
    console.log('not_implemented yet')
}