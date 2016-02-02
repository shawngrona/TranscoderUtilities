import boto3
import sys



def start_transcode(filename, pipelineid, region):
    transcoderClient = boto3.client('elastictranscoder', region_name=region)
    transcoderClient.create_job(
        PipelineId=pipelineid,
        Input={
                'Key': filename,
                'FrameRate': 'auto',
                'Resolution': 'auto',
                'AspectRatio': 'auto',
                'Interlaced': 'auto',
                'Container': 'auto'
        },
            Outputs=[{
                'Key': '.'.join(filename.split('.')[:-1]) + '.mp4',
                'PresetId': '1351620000001-000010'
            }]
        )
    print("Started transcoding {0}".format(filename))

if __name__ == "__main__":
   start_transcode(str(sys.argv[1]),str(sys.argv[2]), str(sys.argv[3]))