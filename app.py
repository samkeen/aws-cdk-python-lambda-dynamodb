#!/usr/bin/env python3

from aws_cdk import cdk

from random_writer.random_writer_stack import RandomWriterStack


app = cdk.App()
RandomWriterStack(app, "random-writer-cdk-1")

app.run()
