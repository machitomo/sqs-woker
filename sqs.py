import boto3

queue_name = "test-sqs"
sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName=queue_name)

def all_get_delete_messages_():
    """ すべてのメッセージを取得、削除する
    """
    message_list = []
    file_path = ""
    counter = 0
    while True:
        # メッセージを取得
        msg_list = queue.receive_messages(MaxNumberOfMessages=10)
        if msg_list:
            for message in msg_list:
                message_list(message.body)
                message.delete()
        elif len(msg_list) == 0 and counter == 10:
            break
        else:
            counter+=1
    if len(message_list) != 0:
        write_message_to_file(file_path,message_list)

def write_message_to_file(file_path,message_list):
    """メッセージを書き出していく
    """
    with open(file_path, "w") as f:
        for message in message_list:
            f.write(message+",\n")
            
def main():
    """メイン関数
    """
    pass

if __name__ == "__main__":
    main()
