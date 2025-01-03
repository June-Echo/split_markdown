from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain.schema import Document


def split_markdown_file_with_langchain(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        headers_to_split_on = [
            ("#", "Header 1")
        ]
        markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)
        splits = markdown_splitter.split_text(content)

        for split in splits:
            if isinstance(split, Document):
                title = split.metadata.get('Header 1')
                sub_content = split.page_content
                sanitized_title = ''.join(c for c in title if c.isalnum() or c == '_')
                sub_file_path = f'D:\\AliDownload\\{sanitized_title}.md'
                with open(sub_file_path, 'w', encoding='utf-8') as sub_f:
                    sub_f.write(f'# {title}\n')
                    sub_f.write(sub_content)
        print('文件拆分完成。')
    except FileNotFoundError:
        print(f'文件 {file_path} 未找到。')
    except Exception as e:
        print(f'发生错误: {e}')


if __name__ == "__main__":
    file_path = r'D:\AliDownload\XXXX.md'
    split_markdown_file_with_langchain(file_path)