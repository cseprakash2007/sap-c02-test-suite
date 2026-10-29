// Q44: source choices preserved in bank order; malformed punctuation repaired.
export const Q44_CORRECTION = {
 stem:'A company wants to migrate an application to Amazon EC2 from VMware Infrastructure that runs in an on-premises data center. A solutions architect must preserve the software and configuration settings during the migration. What should the solutions architect do to meet these requirements?',
 options:[
 {id:'A',text:'Configure the AWS DataSync agent to start replicating the data store to Amazon FSx for Windows File Server. Use the SMB share to host the VMware data store. Use VM Import/Export to move the VMs to Amazon EC2.'},
 {id:'B',text:'Use the VMware vSphere client to export the application as an image in Open Virtualization Format (OVF). Create an Amazon S3 bucket to store the image in the destination AWS Region. Create and apply an IAM role for VM Import. Use the AWS CLI to run the EC2 import command.'},
 {id:'C',text:'Configure AWS Storage Gateway File Gateway to export a Common Internet File System (CIFS) share. Create a backup copy in the shared folder. Sign in to the AWS Management Console and create an AMI from the backup copy. Launch an EC2 instance that is based on the AMI.'},
 {id:'D',text:'Create a managed-instance activation for a hybrid environment in AWS Systems Manager. Download and install Systems Manager Agent on the on-premises VM. Register the VM with Systems Manager to be a managed instance. Use AWS Backup to create a snapshot of the VM and create an AMI. Launch an EC2 instance that is based on the AMI.'}
 ],
 answers:['B'],answerCount:1,
 explanation:'Correct answer B. Export the VMware VM with vSphere, package the VM in an AWS-supported image format (such as OVA or VMDK), upload it to S3 in the destination Region, create the vmimport IAM service role, and run aws ec2 import-image. VM Import/Export creates an AMI from which EC2 can launch with the guest OS and installed applications. The original answer refers to OVF export; an OVF descriptor alone is not a supported import-image disk container, so export/package a supported OVA or VMDK image. Some external answer dumps incorrectly mark D even while explaining the VM Import process.',
 wrongOptionsExplanation:'A: DataSync/FSx handles file transfer and storage, not direct VMware-to-AMI conversion. B: Correct purpose-built VM image import path. C: File Gateway CIFS backups do not directly become AMIs. D: Systems Manager hybrid activation manages on-premises servers but AWS Backup cannot create an EC2 AMI directly from the activated on-premises VM.',
 plainWords:'Preserve the VMware VM operating system, installed software, and configuration by exporting its disk image and importing it as an EC2 AMI.',
 keyPoints:'VMware vSphere export; supported OVA/VMDK formats; S3 in destination Region; vmimport IAM role; aws ec2 import-image; external practice-site answer key disagreement. https://docs.aws.amazon.com/vm-import/latest/userguide/import-vm-image.html',
 sourceWarning:'Question text cleaned from source. Some external sites incorrectly mark option D despite their explanation describing B. OVF export must produce a supported importable OVA or VMDK image.',
 answerStatus:'aws-doc-verified-with-external-key-disagreement'
};
