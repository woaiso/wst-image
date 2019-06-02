import React from 'react';
import {
  Form,
  Row,
  Col,
  Input,
  Select,
  InputNumber,
  Switch,
  Radio,
  Rate,
  Checkbox,
  Upload,
  Button,
  Icon,
  Slider,
} from 'antd';

import styles from './form.css';


const { Option } = Select;

class AnyImageForm extends React.Component<any, any> {
  handleSubmit = () => {};
  normFile = (e: { fileList: any }) => {
    if (Array.isArray(e)) {
      return e;
    }
    return e && e.fileList;
  };
  render() {
    const { getFieldDecorator } = this.props.form;
    const formItemLayout = {
      labelCol: { span: 6 },
      wrapperCol: { span: 14 },
    };
    return (
      <Form {...formItemLayout} onSubmit={this.handleSubmit}>
        <Form.Item label="宽度">
          {getFieldDecorator('width', {
            initialValue: 480,
            rules: [{ required: true, message: '请输入正确的图片宽度!' }],
          })(<InputNumber min={10} max={2048} style={{ width: '100%' }}/>)}
        </Form.Item>
        <Form.Item label="高度">
          {getFieldDecorator('height', {
            rules: [{ required: true, message: '请输入正确的图片高度!' }],
          })(<InputNumber min={10} max={2048} style={{ width: '100%' }}/>)}
        </Form.Item>

        <Form.Item label="背景颜色">
          {getFieldDecorator('bg_color', {
            rules: [],
          })(<Input />)}
        </Form.Item>

        <Form.Item label="文本颜色">
          {getFieldDecorator('color', {
            rules: [],
          })(<Input />)}
        </Form.Item>
        <Form.Item label="图片格式" hasFeedback={true}>
          {getFieldDecorator('format', {
            rules: [{ required: false, message: '请选择一个导出的图片格式' }],
          })(
            <Select placeholder="请选择一个图片格式">
              <Option value="png">png</Option>
              <Option value="gif">gif</Option>
              <Option value="jpg">jpg</Option>
              <Option value="jpeg">jpeg</Option>
            </Select>,
          )}
        </Form.Item>

        <Form.Item label="文件大小(KB)">
          {getFieldDecorator('volume', {
            initialValue: 0,
            rules: [{ required: false, message: '请输入正确的文件大小!' }],
          })(<InputNumber min={0} max={2048} style={{ width: '100%' }}/>)}
        </Form.Item>

        <Form.Item label="文本">
          {getFieldDecorator('text', {
            initialValue: 'anyimage.xyz',
            rules: [],
          })(<Input />)}
        </Form.Item>
        <div>
          <Button type="primary" icon="eye" size="large">预览</Button>
          <Button type="primary" icon="download" size="large">下载</Button>
        </div>
      </Form>
    );
  }
}

export default Form.create({ name: 'any_image_form' })(AnyImageForm);
