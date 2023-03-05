chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {    
    let url = tabs[0].url;
    document.getElementById("url").value=url
});

var json_test = {
    "topic1": ["1","2","3","4"]
}


function jsonToNode(json) {
    node = document.createElement("div")
    node.style.paddingTop = "20px"
    for (let topic in json) {
        text = document.createElement("text")
        name_node = document.createTextNode(topic)
        text.style.fontWeight = "bold"
        text.appendChild(name_node)
        node.appendChild(text)
        break_node = document.createElement("br")
        node.appendChild(break_node)
        
        for (topic_item in json[topic]) {
            console.log(json[topic][topic_item])
            bullet_node = document.createElement("li")
            value_node = document.createTextNode(json[topic][topic_item])
            bullet_node.appendChild(value_node)
            bullet_node.style.paddingLeft = "20px"
            node.appendChild(bullet_node)
            
            break_node = document.createElement("br")
            node.appendChild(break_node)
        }

    }
    console.log(text)
    
    // text_node = document.createTextNode(text)
    // node.appendChild(text_node)
    return node
  }
function createDiv(json){
    // console.log(document.getElementById("containerthing"))   
    document.getElementById("containerthing").appendChild(jsonToNode(json))
}

// createDiv(json_test)