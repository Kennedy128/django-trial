showModal=(name,desc,url, loc,cat) => {
    $("#label").text(name)
    $("#myModal").modal("show")
    $(".mod-img").attr("src",url)
    $("#img-desc").text(desc)
    //$("#url-to-copy").val(window.location.origin + url)
    $("#img-loc").text("Location: " + loc)
    $("#img-cat").text("Category: " + cat)
}