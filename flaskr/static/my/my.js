// $(function () {
//     $("#li-tag").each(function () {
//         $(this).click(function () {
//             $(this).attr('class', 'active')
//             $("#li-tag:not(this)").removeAttr('class')
//         })
//     })
// })

// 时间与日期

// 导航标签切换
$(document).ready(function () {
    // each 是 为每一个匹配的元素 执行定义的方法
    $(".ul_header").find("li").each(function () {
        var a = $(this).find("a:first")[0];
        // location.pathname 获取 当前浏览器上的url 地址
        if ($(a).attr("href") === location.pathname) {
            $(this).addClass("active");
        } else {
            $(this).removeClass("active");
        }
    });

})

// var ul = document.querySelector("ul");
// var N = ul.firstElementChild;
// ul.addEventListener("click", clickHandler);
//
// function clickHandler(e) {
//     if (e.target instanceof HTMLUListElement) return;
//     if (e.target instanceof HTMLLIElement) return;
//     if (N) {
//         N.className = "";
//     }
//     N = e.target.parentElement;
//     N.className = "active";
//
// }


//给当前元素设置新的样式，并删除当前元素的同胞元素的样式

// $('.ul_header').find('li').each(function () {
//        $(this).click(function () {
//            $(this).parent().addClass('active')
//            $(this).parent().siblings().removeClass("active")
//
//            // 或者写成一句
//           //$(this).parent().addClass('active').siblings().removeClass("active")
//        })
//    })


// $('.ul_header').find('li').each(function () {
//     var a = $(this).find("a:first")[0];
//     if ($(a).attr("href") == document.location.href || document.location.href.search(this.href) >= 0) {
//         $(this).addClass('active'); // this.className = 'active';
//     } else {
//         $(this).removeClass("active");
//     }
// });


// 字段detail是要替换的字段

// 上传文件配置
CKEDITOR.replace('details', {
    height: 500, // 编辑器的高度
    filebrowserUploadUrl: '/upload', // 图片文件要上传的路径,加?是为了添加粘贴上传的功能
    disallowedContent: 'img{width,height};img[width,height]' // 去掉上传图片之后，默认添加的width和height
});

