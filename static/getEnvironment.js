//获取用例信息
var EnvironmentInit = function () {

    var url = document.location;
    var eid =  url.pathname.split("/")[2];
//    alert(pid)
    $.post("/get_environment_info/",
    {
//        alert(pid)
        eid: eid,
    },
    function (resp) {
        console.log("返回的结果", resp.data);
        var result = resp.data;
        console.log(result.name)
        //请求URL
        document.querySelector("#environment_name").value = result.name;
        //请求头
        document.querySelector("#environment_address").value = result.address;

    });

}




