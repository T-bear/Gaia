//console.log("Still connected boss")

    // create an array with nodes
    var nodes = new vis.DataSet();
    console.log(nodes)
    // add items
    // note that the data items can contain different properties and data formats
    var data = new vis.DataSet(data);



    // create an array with edges
    //var edges = new vis.DataSet();

{% for house in houses %}

if(!({{ house['city'] }} in nodes)) {

nodes.add({
	id: '{{ loop.index }}',
    label: '{{ house['city'] }}',
    shape: 'box'}
    );

data.add([
  {id: '{{ loop.index }}', text: ['{{house.city}}','{{house.location}}', '{{house.name}}']}
]);
}
{% set node_loop = loop %}

/*
console.log('{{loop}}')
var edges = new vis.DataSet([
        //{from: '{{ node_loop.index}}', to: '{{ node_loop.index }}'},
    ]);
*/
{% endfor %}
    // create a network
    var container = document.getElementById('mynetwork');

    // provide the data in the vis format
    var data = {
        nodes: nodes,
       // edges: edges,
        data: data
    };

    var options = {};
    // initialize your network!
    var network = new vis.Network(container, data, options);
    network.fit();
    network.on( 'click', function(properties) {
    var ids = properties.nodes;

    var city = data.data._data[ids].text[0];
    var location = data.data._data[ids].text[1];
    var name = data.data._data[ids].text[2];

    var clickedNodes = nodes.get(ids);
    if (ids != undefined){
    	$("#myModal").modal();
    	var strLink = "https://155.4.72.38:5000/" + city + "/" + location + "/" + name;
    	var adr = strLink.toLowerCase();

    	document.getElementById("greenhouseLink").setAttribute("href",adr);
    	document.getElementById("city").textContent = city;
    	document.getElementById("location").textContent = location;
    	document.getElementById("name").textContent = name;
};

});
