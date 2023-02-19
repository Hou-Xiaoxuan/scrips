function compress_pdf --description 压缩pdf文件
    argparse a/all s/source -- $argv
    if set -q _flag_all
        for file in *.pdf
            gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dBATCH -dQUIET -sOutputFile="compress_$file" $file
        end
    else if set -q _flag_source
        for file in $argv
            gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dBATCH -dQUIET -sOutputFile="compress_$file" $file
        end
    else
        echo "参数不正确，请使用：
        -a/--all \t\t压缩所有pdf文件
        -s/--source file1.pdf file2.pdf ..."
        return
    end
end