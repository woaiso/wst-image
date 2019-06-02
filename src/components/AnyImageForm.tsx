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
      labelCol: { span: 8 },
      wrapperCol: { span: 16 },
    };
    return (
      <div className={styles['image-form']}>
        <Form {...formItemLayout} onSubmit={this.handleSubmit}>
          <div>
            <h1 className={styles['form-title']}>请填写以下配置</h1>
          </div>
          <Form.Item label="宽度" help="支持范围：10 ~ 2048">
            {getFieldDecorator('width', {
              initialValue: 1080,
              rules: [{ required: true, message: '请输入正确的图片宽度!' }],
            })(<InputNumber min={10} max={2048} style={{ width: '100%' }} />)}
          </Form.Item>
          <Form.Item label="高度" help="支持范围：10 ~ 2048">
            {getFieldDecorator('height', {
              initialValue:480,
              rules: [{ required: true, message: '请输入正确的图片高度!' }],
            })(<InputNumber min={10} max={2048} style={{ width: '100%' }} />)}
          </Form.Item>

          <Form.Item label="圆角" help="支持范围：0 ~ 100">
            {getFieldDecorator('radius', {
              initialValue:0,
              rules: [{ required: false, message: '请输入正确的圆角大小!' }],
            })(<InputNumber min={0} max={100} style={{ width: '100%' }} />)}
          </Form.Item>

          <Form.Item label="内边距" help="参考格式：10 20 10 20">
            {getFieldDecorator('padding', {
              initialValue:0,
              rules: [{ required: false, message: '请输入正确的圆角大小!' }],
            })(<Input style={{ width: '100%' }} />)}
          </Form.Item>

          <Form.Item label="背景颜色">
            {getFieldDecorator('bg_color', {
              initialValue:'#1890FF',
              rules: [],
            })(<Input />)}
          </Form.Item>

          <Form.Item label="文本颜色">
            {getFieldDecorator('color', {
              initialValue:'#FFFFFF',
              rules: [],
            })(<Input />)}
          </Form.Item>
          <Form.Item label="图片格式" hasFeedback={true}>
            {getFieldDecorator('format', {
              initialValue:'png',
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

          <Form.Item label="文件大小(KB)" help="默认使用自动生成的文件大小">
            {getFieldDecorator('volume', {
              initialValue: 0,
              rules: [{ required: false, message: '请输入正确的文件大小!' }],
            })(<InputNumber min={0} max={2048} style={{ width: '100%' }} />)}
          </Form.Item>

          <Form.Item label="文本">
            {getFieldDecorator('text', {
              initialValue: 'anyimage.xyz',
              rules: [],
            })(<Input />)}
          </Form.Item>
          <Row gutter={8}>
            <Col span={12}>
              <div className={styles['gutter-box']}>
                <Button type="default" icon="eye" size="large" style={{ width: '100%' }}>
                  预览
                </Button>
              </div>
            </Col>
            <Col span={12}>
              <div className={styles['gutter-box']}>
                <Button type="primary" icon="download" size="large" style={{ width: '100%' }}>
                  下载
                </Button>
              </div>
            </Col>
          </Row>
        </Form>
      </div>
    );
  }
}

export default Form.create({ name: 'any_image_form' })(AnyImageForm);
